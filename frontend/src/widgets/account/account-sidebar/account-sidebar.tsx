import React from 'react'
import { useAuth0 } from '@auth0/auth0-react'
import { useTranslation } from 'react-i18next'
import { Link, useLocation } from 'react-router-dom'

import { DangerTriangleIcon, DangerTriangleSolidIcon } from '@/shared/ui/icons'
import { ArrowLeftRed } from '@/shared/ui/icons/arrow-left-red.tsx'
import { SIDEBAR_ITEMS } from '@/shared/constants/account-sidebar.const.ts'
import { cn } from '@/shared/library/utils'

interface Props {
  className?: string
}

export const AccountSidebar: React.FC<Props> = ({ className }) => {
  const location = useLocation()
  const activeTab = SIDEBAR_ITEMS.find(item =>
    location.pathname.endsWith(item.url),
  )?.title

  const { t } = useTranslation()
  const { logout, user } = useAuth0()

  return (
    <aside className={cn('w-[305px] shrink-0 border-r', className)}>
      <nav className='space-y-[10px] border-b pb-[30px] pr-[48px] pt-[42px]'>
        {SIDEBAR_ITEMS.map(item => (
          <button
            key={item.title}
            className={`h-[42px] w-full rounded-xl pl-[18px] ${
              activeTab === item.title
                ? 'bg-primary-500 text-gray-50'
                : 'text-gray-900'
            }`}
          >
            <Link
              to={item.url}
              className='flex items-center gap-2 text-sm font-[500]'
            >
              {activeTab === item.title ? (
                <item.icon.solid />
              ) : (
                <item.icon.outline />
              )}
              {t(`${item.title}`)}
              {item.title === 'account.profile' && !user?.email_verified && (
                <>
                  {activeTab === 'account.profile' ? (
                    <DangerTriangleSolidIcon className='ml-auto mr-[18px] h-5 w-5 text-error-400' />
                  ) : (
                    <DangerTriangleIcon className='ml-auto mr-[18px] h-5 w-5' />
                  )}
                </>
              )}
            </Link>
          </button>
        ))}
      </nav>
      <button
        onClick={() => logout()}
        className='mt-[30px] flex h-8 w-full items-center gap-[17px] pl-[18px] text-left text-sm text-error-700'
      >
        <ArrowLeftRed />
        {t('account.logOut')}
      </button>
    </aside>
  )
}
